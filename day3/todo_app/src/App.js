import React, { useState, useEffect } from 'react';
import { Button, FormControl, Input, InputLabel } from '@material-ui/core';
// import { FormControl } from '@material-ui/core';
import './App.css';
import Todo from './Todo';
import db from './firebase';
import firebase from 'firebase';

function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  //To check whether our input is getting added to the input list
  //-> console.log(input)

  //When theapp loads, we need to listen to the databse and fetch new todos as they get removed/added
  //this fires up when app.js loads

  useEffect (() => {
    db.collection('todos').orderBy('timestamp', 'desc').onSnapshot(snapshot => {
      //We .todo because firebase will retutn the whole bunch of array objects -> run this next line anc check it out
      //click this in chrome inspect console - {{}}
      //console.log(snapshot.docs.map(doc => doc.data()));
      setTodos(snapshot.docs.map(doc => ({id: doc.id, todo: doc.data().todo})))
    })
  }, []);

  //We need to listener only once

  const addTodo = (event) => {
    //When you click submit the page will automatically be refreshed so we have to prevent it
    event.preventDefault(); //will prevent refresh
    db.collection('todos').add({
      todo: input,
      timestamp: firebase.firestore.FieldValue.serverTimestamp()
      //we are converting into a todo object
    })
    setTodos([...todos, input]);
    setInput(''); //clear up the input after clicking submit

    //we are spreading out todos which means
    //we are appending input to todo without deleting the element which were already there
    //REMEMBER todos is in short time memory as it is a state variable
  }
  return (
    <div className="App">
      <h1>This is my first react app</h1>

      <FormControl>
        <InputLabel>Write a Todo</InputLabel>
        <Input value={input} onChange={event =>setInput(event.target.value)}/>
        <Button disabled={!input} type="submit" onClick={addTodo}variant="contained" color="primary">
          Add todo
        </Button>
      </FormControl>

      <ul>
        {todos.map(todo => (
          <Todo todo={todo}/>
          // <li>{todo}</li>
        ))}
      </ul>

    </div>
  );
}

export default App;
