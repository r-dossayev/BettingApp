import React, {useEffect} from 'react';
import {useTypedSelector} from "../hooks/useTypedSelector";
import {fetchLeagues} from "../store/actionCreators/leagues";
import {useDispatch} from "react-redux";
import "../styles/basic.css";

const LeagueList: React.FC = () => {
    const {leagues,} = useTypedSelector(state1 => state1.leagues) // all state in redux
    const dispatch = useDispatch(); //dispatch
    useEffect(() => {
        // @ts-ignore
        dispatch(fetchLeagues())
    }, [])
    console.log(leagues)
    return (
        <div>
            {leagues?.map((league: any) => {
                return (<div key={league.id} className="card-container">
                    <div className="card u-clearfix">
                        <div className="card-body">
                            <span className="card-number card-circle subtle">{league.id}</span>
                            <span className="card-author subtle">{league.country}</span>
                            <h2 className="card-title">{league.name}</h2>
                            <span className="card-description subtle">These last few weeks I have been working hard on a new brunch recipe for you all.</span>
                            <div className="card-read">Read</div>
                            <span className="card-tag card-circle subtle">C</span>
                        </div>
                        <img src={league.poster} alt="" className="card-media"/>
                    </div>
                    <div className="card-shadow"></div>
                </div>)
            })}
        </div>

    );
};

export default LeagueList;