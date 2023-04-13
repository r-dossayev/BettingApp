import {Dispatch} from "redux";
import axios from "axios";
import {ClubsActionCreators, LCActionType} from "../types/LeagueClubsType";

export const fetchLeagueClubs = (id: number) => {
    return async (dispatch: Dispatch<ClubsActionCreators>) => {
        try {
            dispatch({type: LCActionType.FETCH_CLUBS})
            const response = await axios.get(`http://localhost:8000/api/alpha/leagues/${id}/clubs/`)
            dispatch({type: LCActionType.FETCH_CLUBS_SUCCESS, payload: response.data})
        } catch (e) {
            dispatch({type: LCActionType.FETCH_CLUBS_ERROR, payload: 'error server league clubs'})
        }
    }
}