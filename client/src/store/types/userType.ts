export interface userType {
    user: any,
    isAuth: boolean,
    error: null | string,
}

export enum actionType {
    FETCH_USER = "FETCH_USER",
    FETCH_USER_ERROR = "FETCH_USER_ERROR",
    FETCH_USER_SUCCESS = "FETCH_USER_SUCCESS"
}


interface fetchUserError {
    type: actionType.FETCH_USER_ERROR
    payload: string
}


interface fetchUser {
    type: actionType.FETCH_USER
}

interface fetchUserSuccess {
    type: actionType.FETCH_USER_SUCCESS
    payload: any
}

export type UserAction = fetchUser | fetchUserError | fetchUserSuccess
