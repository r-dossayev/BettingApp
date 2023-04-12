import {LeaguesActionType, LGActionType} from "../types/leagueType";
import {Dispatch} from "redux";
import axios from "axios";

export const fetchLeagues = () => {
    return async (dispatch: Dispatch<LeaguesActionType>) => {
        try {
            dispatch({type: LGActionType.FETCH_LEAGUES})
            const response = await axios.get('http://127.0.0.1:8000/api/alpha/leagues/')
            dispatch({type: LGActionType.FETCH_LEAGUES_SUCCESS, payload: response.data})
        } catch (e) {
            dispatch({type: LGActionType.FETCH_LEAGUES_ERROR, payload: 'error'})
        }
    }
}