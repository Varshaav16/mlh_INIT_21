import { List, ListItem, ListItemText, Modal } from '@material-ui/core';
import './Todo.css';
import React, {useState} from 'react';
import db from './firebase';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import { makeStyles } from '@material-ui/core/styles';

//component -> is something(an element -> button, row etc) we create and once we reuse it
//and we only have one piece of code to change it
//props -> properties - which helps us to differentiate components

const useStyles = makeStyles((theme) => ({
    paper: {
      position: 'absolute',
      width: 400,
      backgroundColor: theme.palette.background.paper,
      border: '2px solid #000',
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
    },
  }));

function Todo(props) {

    const classes = useStyles();
    const [open, setOpen] = useState(false);
    const [input, setInput] = useState('');


    const handleClose = () => {
        setOpen(false);
    };

    const handleOpen = () => {
        setOpen(true);
    };

    const updateTodo = () => {
        db.collection('todos').doc(props.todo.id).set({
            todo: input
        }, {merge: true});
        setOpen(false);
    }

    return (
        <>
        <Modal
            open={open}
            onClose={handleClose}
        >
            <div className={classes.paper}>
                <h1>Update todo</h1>
                <input placeholder={props.todo.todo} value={input} onChange={event => setInput(event.target.value)} />
                <button onClick={updateTodo}>Update todo</button>
            </div>
        </Modal>
        <List className="todo__list">
            <ListItem>
                <ListItemText primary={props.todo.todo} secondary="Complete it soon!" />
            </ListItem>
            <EditIcon onClick={e => setOpen(true)} />
            <DeleteIcon onClick={event=> db.collection('todos').doc(props.todo.id).delete()} />
        </List>
        </> //wrap segment to wrap two or more things
    )
}

export default Todo;
