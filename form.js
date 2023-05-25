import React, { useState } from 'react';
import './form.css'; // Import the CSS file

function Form() {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [favoriteSport, setFavoriteSport] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Create an object with the form data
    const formData = {
      name,
      age,
      gender,
      favoriteSport
    };

    // Send the form data to the backend
    fetch('http://127.0.0.1:5000/save-data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then(response => response.json())
      .then(data => {
        console.log('Data saved:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });

    // Clear the form inputs
    setName('');
    setAge('');
    setGender('');
    setFavoriteSport('');
  };

  const ageOptions = [];
  for (let i = 10; i <= 25; i++) {
    ageOptions.push(<option key={i} value={i}>{i}</option>);
  }

  const sportsOptions = [
    'Kabaddi',
    'Cricket',
    'Badminton',
    'Kho Kho',
    'Volleyball',
    'Chess',
    'Carrom',
    'Football',
    'Swimming'
  ];

  return (
    <div>
      <h3 className="form-heading">Fill out the form</h3>
      <form onSubmit={handleSubmit} className="form">
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required className="form-input" />
        </label>
        <br />
        <label>
          Age:
          <select value={age} onChange={(e) => setAge(e.target.value)} required className="form-select">
            <option value="">Select</option>
            {ageOptions}
          </select>
        </label>
        <br />
        <label>
          Gender:
          <select value={gender} onChange={(e) => setGender(e.target.value)} required className="form-select">
            <option value="">Select</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </label>
        <br />
        <label>
          Favorite Sport:
          <select value={favoriteSport} onChange={(e) => setFavoriteSport(e.target.value)} required className="form-select">
            <option value="">Select</option>
            {sportsOptions.map(sport => (
              <option key={sport} value={sport}>{sport}</option>
            ))}
          </select>
        </label>
        <br />
        <button type="submit" className="form-button">Submit</button>
      </form>
    </div>
  );
}

export default Form;
