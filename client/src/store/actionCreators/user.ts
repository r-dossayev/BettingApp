import {Dispatch} from "redux";
import axios from "axios";
import {actionType, UserAction} from "../types/userType";

export const fetchUser = () => {
    return async (dispatch: Dispatch<UserAction>) => {
        try {
            dispatch({type: actionType.FETCH_USER})
            const response = await axios.get('http://127.0.0.1:8000/api/alpha/leagues/')
            dispatch({type: actionType.FETCH_USER_SUCCESS, payload: response.data})
        } catch (e) {
            dispatch({type: actionType.FETCH_USER_ERROR, payload: 'error '})
        }
    }
}