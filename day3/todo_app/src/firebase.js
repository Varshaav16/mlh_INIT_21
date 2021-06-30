

// For Firebase JS SDK v7.20.0 and later, measurementId is optional

import firebase from "firebase";

const firebaseApp = firebase.initializeApp({
    apiKey: "AIzaSyDGK0Kq4lRI9P8pN1o4FOlT7G5g-D58ECI",
    authDomain: "react-todo-app1.firebaseapp.com",
    projectId: "react-todo-app1",
    storageBucket: "react-todo-app1.appspot.com",
    messagingSenderId: "221223260095",
    appId: "1:221223260095:web:8c0454ef5e9f2bfa439b0a",
    measurementId: "G-YLNKZYV13Y"

});

const db = firebaseApp.firestore();

export default db;