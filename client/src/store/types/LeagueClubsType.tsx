export interface clubsType {
    clubs: any,
    loading: boolean,
    error: null | string,
}

export enum LCActionType {
    FETCH_CLUBS = "FETCH_CLUBS",
    FETCH_CLUBS_SUCCESS = "FETCH_CLUBS_ERROR",
    FETCH_CLUBS_ERROR = "FETCH_CLUBS_SUCCESS"
}


interface fetchClubsError {
    type: LCActionType.FETCH_CLUBS_ERROR
    payload: string
}


interface fetchClubs {
    type: LCActionType.FETCH_CLUBS
}

interface fetchClubsSuccess {
    type: LCActionType.FETCH_CLUBS_SUCCESS
    payload: any[]
}

export type ClubsActionCreators = fetchClubsError | fetchClubs | fetchClubsSuccess
