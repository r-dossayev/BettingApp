import React from 'react';
import Navbar from "./components/Navbar/Navbar";
import {Route, Routes} from "react-router-dom";
import Register from "./components/Register";
import LeagueList from "./components/LeagueList";
import Login from "./components/Login";
import Home from "./components/Home";

function App() {


    return (
        <div>
            <Navbar/>
            <Routes>
                <Route path={'/'} element={<Home/>}/>
                <Route path={'/login'} element={<Login/>}/>
                <Route path={'/register'} element={<Register/>}/>
                <Route path={'/leagues'} element={<LeagueList/>}/>
                {/*<Route path={'/leagues/:id'} element={<LeagueList/>}/>*/}
            </Routes>
        </div>

    );
}

export default App;
