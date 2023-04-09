import {LGActionType, LeaguesActionType, leagueType} from "../types/leagueType";


const initialState: leagueType = {
    loading: true,
    leagues: null,
    error: null,

};
export const leagueReducer = (state = initialState, action: LeaguesActionType): leagueType => {
    switch (action.type) {
        case LGActionType.FETCH_LEAGUES:
            return {loading: true, error: null, leagues: {}}
        case LGActionType.FETCH_LEAGUES_SUCCESS:
            return {loading: false, error: null, leagues: action.payload}
        case LGActionType.FETCH_LEAGUES_ERROR:
            return {loading: false, error: action.payload, leagues: action.payload}
        default:
            return state
    }

}
