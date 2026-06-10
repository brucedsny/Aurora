import argparse
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:  # pragma: no cover - optional dependency for local execution
    service_account = None
    build = None


SCOPES = ["https://www.googleapis.com/auth/drive"]


@dataclass
class DriveFile:
    file_id: str
    name: str
    mime_type: str
    created_time: str
    modified_time: str
    size: str = ""
    md5_checksum: str = ""

    @property
    def dedupe_key(self) -> Tuple[str, str, str]:
        if self.md5_checksum and self.size:
            return (self.md5_checksum, self.size, self.mime_type)
        return (self.name, self.size, self.mime_type)

    @property
    def created_at(self) -> datetime:
        return datetime.fromisoformat(self.created_time.replace("Z", "+00:00"))


class GoogleDriveDuplicateCleanerAgent:
    def __init__(self, service, dry_run: bool = True):
        self.service = service
        self.dry_run = dry_run

    def _list_files(self) -> List[DriveFile]:
        results: List[DriveFile] = []
        page_token = None
        while True:
            response = (
                self.service.files()
                .list(
                    q="trashed = false and mimeType != 'application/vnd.google-apps.folder'",
                    fields=(
                        "nextPageToken, files(id,name,mimeType,size,md5Checksum,"
                        "createdTime,modifiedTime)"
                    ),
                    pageSize=1000,
                    pageToken=page_token,
                )
                .execute()
            )
            for file_data in response.get("files", []):
                results.append(
                    DriveFile(
                        file_id=file_data["id"],
                        name=file_data["name"],
                        mime_type=file_data.get("mimeType", ""),
                        size=file_data.get("size", ""),
                        md5_checksum=file_data.get("md5Checksum", ""),
                        created_time=file_data.get("createdTime", "1970-01-01T00:00:00Z"),
                        modified_time=file_data.get("modifiedTime", "1970-01-01T00:00:00Z"),
                    )
                )
            page_token = response.get("nextPageToken")
            if not page_token:
                break
        return results

    def find_duplicate_groups(self) -> Dict[Tuple[str, str, str], List[DriveFile]]:
        grouped: Dict[Tuple[str, str, str], List[DriveFile]] = {}
        for drive_file in self._list_files():
            if not drive_file.size:
                continue
            grouped.setdefault(drive_file.dedupe_key, []).append(drive_file)
        return {key: files for key, files in grouped.items() if len(files) > 1}

    def clean_duplicates(self) -> List[str]:
        actions: List[str] = []
        duplicate_groups = self.find_duplicate_groups()

        for files in duplicate_groups.values():
            ordered = sorted(files, key=lambda current: current.created_at)
            keep = ordered[0]
            for duplicate in ordered[1:]:
                action = f"Keep {keep.name} ({keep.file_id}) | Trash {duplicate.file_id}"
                actions.append(action)
                if not self.dry_run:
                    self.service.files().update(
                        fileId=duplicate.file_id,
                        body={"trashed": True},
                    ).execute()
        return actions


def build_service(credentials_path: str, delegated_user: str = ""):
    if service_account is None or build is None:
        raise RuntimeError(
            "Missing dependencies. Install google-api-python-client and google-auth."
        )

    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    if delegated_user:
        credentials = credentials.with_subject(delegated_user)
    return build("drive", "v3", credentials=credentials)


def main():
    parser = argparse.ArgumentParser(
        description="Agent to find and clean duplicate files in Google Drive."
    )
    parser.add_argument("--credentials", required=True, help="Service account JSON path.")
    parser.add_argument(
        "--delegated-user",
        default="",
        help="Workspace user email for domain-wide delegation.",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Execute deletion by moving duplicates to trash. Default is dry-run.",
    )
    args = parser.parse_args()

    service = build_service(args.credentials, args.delegated_user)
    cleaner = GoogleDriveDuplicateCleanerAgent(service, dry_run=not args.delete)
    planned_actions = cleaner.clean_duplicates()

    if not planned_actions:
        print("No duplicates found.")
        return

    mode = "DRY-RUN" if not args.delete else "EXECUTION"
    print(f"{mode}: {len(planned_actions)} duplicate files identified.")
    for action in planned_actions:
        print(action)


if __name__ == "__main__":
    main()
