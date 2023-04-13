import {ClubsActionCreators, clubsType, LCActionType} from "../types/LeagueClubsType";


const initialState: clubsType = {
    loading: false,
    clubs: null,
    error: null,

};
export const LeagueClubsReducer = (state = initialState, action: ClubsActionCreators): clubsType => {
    switch (action.type) {
        case LCActionType.FETCH_CLUBS:
            return {loading: true, error: null, clubs: null}
        case LCActionType.FETCH_CLUBS_SUCCESS:
            return {loading: false, error: null, clubs: action.payload}
        case LCActionType.FETCH_CLUBS_ERROR:
            return {loading: false, error: action.payload, clubs: null}
        default:
            return state
    }

}
