import React, {useEffect} from 'react';
import {Navigate, useParams} from "react-router-dom";
import {useTypedSelector} from "../hooks/useTypedSelector";
import {useDispatch} from "react-redux";
import {fetchLeagueClubs} from "../store/actionCreators/clubs";

// @ts-ignore
const LeagueClubs: React.FC = () => {
    const {id} = useParams();
    const leagues = useTypedSelector(state1 => state1.leagues.leagues)
    const {clubs, error, loading} = useTypedSelector(state => state.leagueClubs)
    const dispatch = useDispatch()
    // @ts-ignore
    useEffect(() => {
        if (id && leagues && id <= leagues?.length) {
            // @ts-ignore
            dispatch(fetchLeagueClubs(id))
        } else return <Navigate to={'/'}/>
    }, [dispatch])
    if (error || loading || !clubs) {
        return <div>{error ? error : "loading..."}</div>
    }
    return (
        <div>
            <table>
                <tr>
                    <th>poster</th>
                    <th>name</th>
                    <th>draw</th>
                    <th>loses</th>
                    <th>wins</th>
                    <th>point</th>
                </tr>
                {clubs?.map((club: any) =>
                    (<tr key={club.id}>
                        <td><img width="80" height="80" src={club.poster} alt="..."/></td>
                        <td>{club.name}</td>
                        <td>{club.draw}</td>
                        <td>{club.loses}</td>
                        <td>{club.wins}</td>
                        <td>{club.point}</td>
                    </tr>)
                )}

            </table>
        </div>
    );

};

export default LeagueClubs;