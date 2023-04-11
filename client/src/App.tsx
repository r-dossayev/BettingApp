import React, {useEffect, useState} from 'react';
import './App.css';
import {useDispatch} from "react-redux";
import {fetchUser} from "./store/actionCreators/user";
import {useTypedSelector} from "./hooks/useTypedSelector";

function App() {
    const {user} = useTypedSelector(state1 => state1.authUser)
    const dispatch = useDispatch()
    // @ts-ignore
    useEffect(() => {
        // @ts-ignore
        dispatch(fetchUser())
    }, [])

    return (
        <div className="App">
            {user?.map((u:any )=> <div key={u.id}><img src={u.poster} alt=""/> {u.name}</div>)}
        </div>
    );
}

export default App;
