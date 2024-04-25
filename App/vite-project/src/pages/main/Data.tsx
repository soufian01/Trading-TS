import React, { useState, useEffect } from 'react';

function Data() {
    const [data, setData] = useState(null);
    const [postData, setPostData] = useState(null);

    useEffect(() => {
        fetch('http://localhost:5010/data')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setData(data);
            })
            .catch(error => console.error('Errore:', error));
    }, []);

    const handlePostData = () => {
        fetch('http://localhost:5010/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ /* dati da inviare */ })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setPostData(data);
        })
        .catch(error => console.error('Errore:', error));
    };

    return (
        <div>
            <h1>Dati dal backend:</h1>
            {data && <p>{JSON.stringify(data)}</p>}
            <button onClick={handlePostData}>Invia dati al backend</button>
            {postData && <p>{JSON.stringify(postData)}</p>}
        </div>
    );
}

export default Data;
