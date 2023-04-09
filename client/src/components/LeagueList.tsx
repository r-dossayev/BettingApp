import React, {useEffect} from 'react';
import {useTypedSelector} from "../hooks/useTypedSelector";
import {fetchLeagues} from "../store/actionCreators/leagues";
import {useDispatch} from "react-redux";

const LeagueList:React.FC = () => {
    const {leagues, loading, error} = useTypedSelector(state1 => state1.leagues) // all state in redux
    const dispatch = useDispatch(); //dispatch
    useEffect(()=>{
        // @ts-ignore
        dispatch(fetchLeagues())
    },[])
    if (loading)
        return <div>loading...</div>
    if (error)
        return <div>error:{error}</div>
    return (
        <div>
            {leagues[0]}
        </div>
    );
};

export default LeagueList;