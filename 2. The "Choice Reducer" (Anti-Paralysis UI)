import React, { useState } from 'react';

const ChoiceReducer = ({ tasks }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  // If we have parsed through all options
  if (currentIndex >= tasks.length) {
    return <h2>Great job! You have completed your planning for today.</h2>;
  }

  // Strictly limit the UI to 2 choices at a time
  const optionA = tasks[currentIndex];
  const optionB = tasks[currentIndex + 1] || "Nothing right now";

  const handleSelection = (selectedTask) => {
    console.log(`[Action] User selected: ${selectedTask}`);
    // Move to the next pair of choices
    setCurrentIndex(currentIndex + 2); 
  };

  return (
    <div className="choice-container" style={{ textAlign: 'center', padding: '2rem' }}>
      <h1>What would you prefer to do next?</h1>
      
      <div className="binary-buttons" style={{ display: 'flex', gap: '2rem', justifyContent: 'center' }}>
        <button 
          onClick={() => handleSelection(optionA)}
          style={{ padding: '2rem', fontSize: '1.5rem', borderRadius: '12px', backgroundColor: '#4CAF50', color: 'white' }}>
          {optionA}
        </button>

        <button 
          onClick={() => handleSelection(optionB)}
          style={{ padding: '2rem', fontSize: '1.5rem', borderRadius: '12px', backgroundColor: '#2196F3', color: 'white' }}>
          {optionB}
        </button>
      </div>
    </div>
  );
};

// Usage: <ChoiceReducer tasks={["Take Blood Pressure Meds", "Call Grandson", "Drink Water", "Read Newspaper"]} />
