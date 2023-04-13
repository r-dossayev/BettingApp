export interface leagueType {
    leagues: any,
    loading: boolean,
    error: null | string,
}

export enum LGActionType {
    FETCH_LEAGUES = "FETCH_LEAGUE",
    FETCH_LEAGUES_SUCCESS = "FETCH_LEAGUE_ERROR",
    FETCH_LEAGUES_ERROR = "FETCH_LEAGUE_SUCCESS"
}


interface fetchLeaguesError {
    type: LGActionType.FETCH_LEAGUES_ERROR
    payload: string
}


interface fetchLeagues {
    type: LGActionType.FETCH_LEAGUES
}

interface fetchLeaguesSuccess {
    type: LGActionType.FETCH_LEAGUES_SUCCESS
    payload: any[]
}

export type LeaguesActionType = fetchLeaguesError | fetchLeagues | fetchLeaguesSuccess
