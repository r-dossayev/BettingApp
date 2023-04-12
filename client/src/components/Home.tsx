import React, {useEffect} from 'react';
import {useTypedSelector} from "../hooks/useTypedSelector";
import {useDispatch} from "react-redux";
import {fetchUser} from "../store/actionCreators/user";

const Home: React.FC = () => {
     const {user} = useTypedSelector(state1 => state1.authUser)
    const dispatch = useDispatch()
    useEffect(() => {
        // @ts-ignore
        dispatch(fetchUser())
    }, [dispatch])
    return (
        <div>
            <div className="App">
                {user?.map((u: any) => <div key={u.id}><img src={u.poster} alt=""/> {u.name}</div>)}
            </div>
        </div>
    );
};

export default Home;