import {applyMiddleware, combineReducers, createStore} from 'redux'
import thunk from "redux-thunk";
import {userReducer} from "./reducers/userReducer";
import {leagueReducer} from "./reducers/leagueReducer";
import {LeagueClubsReducer} from "./reducers/LeagueClubsReducer";


export const rootReducer = combineReducers({
    authUser: userReducer,
    leagues: leagueReducer,
    leagueClubs:LeagueClubsReducer,
})
export const store = createStore(rootReducer, applyMiddleware(thunk))

export type RootState = ReturnType<typeof rootReducer>