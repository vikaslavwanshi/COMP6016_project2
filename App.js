// import React, { useState } from 'react';
// import FileInput from './component/inputfile';
// import ResultDisplay from './component/resultdisplay';
// import MyNavbar from './component/navbar';
// import ProfileCover from './component/cover';
// import 'bootstrap/dist/css/bootstrap.min.css';

// const App = () => {
//   const [result, setResult] = useState('');
//   const file1Label = "Raw Dataset File";
//   const file2Label = "Test file";

//   const [file1, setFile1] = useState(null);
//   const [file2, setFile2] = useState(null);

//   const handleFile1Change = (file) => {
//     setFile1(file);
//   };

//   const handleFile2Change = (file) => {
//     setFile2(file);
//   };

//   const handleUpload = async () => {
//     if (file1 && file2) {
//       const formData = new FormData();
//       formData.append('raw_data_file', file1);
//       formData.append('test_data_file', file2);
  
//       try {
//         const response = await fetch('http://localhost:8000/predict', {
//           method: 'POST',
//           body: formData,
//         });
  
//         const result = await response.json();
//         setResult(result);
//       } catch (error) {
//         console.error('Error:', error);
//       }
//     }
//   };  

//   return (
//     <div>
//       <MyNavbar />
//       <ProfileCover />
//       <div className="container">
//         <h1>File Upload</h1>
//         <div className="row">
//           <div className="col-md-6">
//             <FileInput label={file1Label} onFileChange={handleFile1Change} />
//           </div>
//           <div className="col-md-6">
//             <FileInput label={file2Label} onFileChange={handleFile2Change} />
//           </div>
//         </div>
//         <button onClick={handleUpload} className="btn btn-primary mt-3">Upload and Predict</button>
//         <ResultDisplay result={result} />
//       </div>
//     </div>
//   );
// };

// export default App;

// import React, { useState } from 'react';
// import FileInput from './component/inputfile';
// import ResultDisplay from './component/ResultDisplay'; // Ensure the file name matches
// import LogDisplay from './component/LogDisplay'; // Ensure the file name matches
// import MyNavbar from './component/navbar';
// import ProfileCover from './component/cover';
// import 'bootstrap/dist/css/bootstrap.min.css';

// const App = () => {
//   const [result, setResult] = useState('');
//   const [trafficData, setTrafficData] = useState(null);
//   const file1Label = "Raw Dataset File";
//   const file2Label = "Test file";

//   const [file1, setFile1] = useState(null);
//   const [file2, setFile2] = useState(null);

//   const handleFile1Change = (file) => {
//     setFile1(file);
//   };

//   const handleFile2Change = (file) => {
//     setFile2(file);
//   };

//   const handleUpload = async () => {
//     if (file1 && file2) {
//       const formData = new FormData();
//       formData.append('raw_data_file', file1);
//       formData.append('test_data_file', file2);
  
//       try {
//         const response = await fetch('http://localhost:8001/predict', {
//           method: 'POST',
//           body: formData,
//         });
  
//         const result = await response.json();
//         setResult(result);
//         // Fetch traffic data after uploading files
//         handleTrafficData(); // Call the function here
//       } catch (error) {
//         console.error('Error:', error);
//       }
//     }
//   };

//   const handleTrafficData = async () => {
//     try {
//       const response = await fetch('http://localhost:8001/process_traffic', {
//         method: 'POST',
//         // Include any necessary traffic data in the request body
//       });

//       const data = await response.json();
//       setTrafficData(data); // Set the traffic data received from the backend
//     } catch (error) {
//       console.error('Error fetching traffic data:', error);
//     }
//   };

//   return (
//     <div>
//       <MyNavbar />
//       <ProfileCover />
//       <div className="container">
//         <h1>File Upload</h1>
//         <div className="row">
//           <div className="col-md-6">
//             <FileInput label={file1Label} onFileChange={handleFile1Change} />
//           </div>
//           <div className="col-md-6">
//             <FileInput label={file2Label} onFileChange={handleFile2Change} />
//           </div>
//         </div>
//         <button onClick={handleUpload} className="btn btn-primary mt-3">Upload and Predict</button>
//         <ResultDisplay result={result} trafficData={trafficData} />
//         <LogDisplay trafficData={trafficData} />
//       </div>
//     </div>
//   );
// };

// export default App;

import React, { useState, useEffect } from 'react';
import MyNavbar from './component/navbar';
import ProfileCover from './component/cover';
import LogDisplay from './component/LogDisplay'; // Assuming you have this
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => {
  const [isRunning, setIsRunning] = useState(false); // Track button toggle
  const [logs, setLogs] = useState(''); // To hold the logs data
  const [error, setError] = useState(null); // To capture any errors

  const handleToggle = async () => {
    setIsRunning((prevState) => !prevState); // Toggle button state
  
    const formData = new FormData();
    const datasetFile = new Blob(["Your dataset contents here"], { type: 'text/csv' });
    formData.append('dataset_file', datasetFile, 'modified_SWaT_Dataset.csv'); // Ensure to append the correct dataset file
  
    try {
      // API call to backend to trigger Mininet script
      const response = await fetch('http://localhost:8001/simulate_attack', {
        method: 'POST',
        body: formData, // Send FormData object
      });
  
      if (response.ok) {
        const data = await response.json();
        setLogs((prevLogs) => prevLogs + '\n' + data.message); // Append new log
      } else {
        setError('Failed to trigger the attack simulation.');
      }
    } catch (error) {
      setError('Error occurred while connecting to backend.');
      console.error(error);
    }
  };

  // Fetch logs periodically
  useEffect(() => {
    const intervalId = setInterval(async () => {
      try {
        const response = await fetch('http://localhost:8001/logs'); // API to get logs
        if (response.ok) {
          const data = await response.json(); // Assuming logs API returns JSON
          setLogs((prevLogs) => prevLogs + '\n' + data.logs.join('\n')); // Append new logs
        } else {
          setError('Failed to fetch logs.');
        }
      } catch (error) {
        setError('Error fetching logs.');
        console.error(error);
      }
    }, 120000); // Fetch logs every 45 seconds

    return () => clearInterval(intervalId); // Cleanup on component unmount
  }, []);

  return (
    <div>
      <MyNavbar />
      <ProfileCover />
      <div className="container">
        <h1>Mininet Traffic Simulation</h1>
        <button
          onClick={handleToggle}
          className={`btn ${isRunning ? 'btn-success' : 'btn-primary'}`}
        >
          {isRunning ? 'Running...' : 'Start Simulation'}
        </button>

        {error && <div className="alert alert-danger mt-3">{error}</div>}

        <LogDisplay logs={logs} />
      </div>
    </div>
  );
};

export default App;
