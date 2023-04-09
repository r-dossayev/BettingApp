import {LeaguesActionType, LGActionType} from "../types/leagueType";
import {Dispatch} from "redux";
import axios from "axios";

export const fetchLeagues = () => {
    return async (dispatch: Dispatch<LeaguesActionType>) => {
        try {
            dispatch({type: LGActionType.FETCH_LEAGUES})
            const response = await axios.get('https://jsonplaceholder.typicode.com/posts')
            dispatch({type: LGActionType.FETCH_LEAGUES_SUCCESS, payload: response.data})
        } catch (e) {
            dispatch({type: LGActionType.FETCH_LEAGUES_ERROR, payload: 'error '})
        }
    }
}