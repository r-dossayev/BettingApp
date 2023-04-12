import {applyMiddleware, combineReducers, createStore} from 'redux'
import thunk from "redux-thunk";
import {userReducer} from "./reducers/userReducer";
import {leagueReducer} from "./reducers/leagueReduser";


export const rootReducer = combineReducers({
    authUser: userReducer,
    leagues: leagueReducer
})
export const store = createStore(rootReducer, applyMiddleware(thunk))

export type RootState = ReturnType<typeof rootReducer>