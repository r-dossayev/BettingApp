import {actionType, UserAction, userType} from "../types/userType";


const initialState: userType = {
    user: null,
    isAuth: false,
    error: null,

};
export const userReducer = (state = initialState, action: UserAction): userType => {
    switch (action.type) {
        case actionType.FETCH_USER:
            return {isAuth: true, error: null, user: null}
        case actionType.FETCH_USER_SUCCESS:
            return {isAuth: false, error: null, user: action.payload}
        case actionType.FETCH_USER_ERROR:
            return {isAuth: false, error: action.payload, user: action.payload}
        default:
            return state
    }

}
