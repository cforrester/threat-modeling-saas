import React, { useEffect, useState } from 'react';
import api from '../api'; // Path depends on where your Axios instance is located

function ThreatModels() {
  const [threatModels, setThreatModels] = useState([]);
  const [error, setError] = useState(null);

  // Fetch data on component mount
  useEffect(() => {
    fetchThreatModels();
  }, []);

  // Function to call the FastAPI endpoint
  const fetchThreatModels = () => {
    api.get('/threat-models')
      .then((response) => {
        setThreatModels(response.data);
      })
      .catch((err) => {
        setError(err.message);
      });
  };

  return (
    <div className="container mt-4">
      <h1>Threat Models</h1>

      {error && (
        <div className="alert alert-danger">
          <strong>Error:</strong> {error}
        </div>
      )}

      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Created By</th>
            <th>Created At</th>
            <th>Components</th>
            <th>Threats</th>
          </tr>
        </thead>
        <tbody>
          {threatModels.map((model) => (
            <tr key={model.id}>
              <td>{model.name}</td>
              <td>{model.created_by}</td>
              <td>{model.created_at}</td>
              <td>
                {model.components && model.components.length > 0 ? (
                  <ul>
                    {model.components.map((comp, index) => (
                      <li key={index}>{comp.name}</li>
                    ))}
                  </ul>
                ) : (
                  'No components'
                )}
              </td>
              <td>
                {model.threats && model.threats.length > 0 ? (
                  <ul>
                    {model.threats.map((threat, index) => (
                      <li key={index}>
                        {threat.name} ({threat.risk_level})
                      </li>
                    ))}
                  </ul>
                ) : (
                  'No threats'
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ThreatModels;
