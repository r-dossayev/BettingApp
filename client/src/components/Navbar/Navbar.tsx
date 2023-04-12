import React from 'react';
import styles from "../../styles/index.module.css";
import {useTypedSelector} from "../../hooks/useTypedSelector";
import {Link} from "react-router-dom";

const Navbar: React.FC = () => {
    const {isAuth} = useTypedSelector(state1 => state1.authUser)
    return (
        <div className={styles.navbar}>
            <div className={styles.logo}>1 x BET</div>
            <div className={styles.navButtons}>
                <Link to={'/'} className={styles.navButton}>Home</Link>
                <Link to={'/'} className={styles.navButton}>About</Link>
                <Link to={'/leagues'} className={styles.navButton}>Football</Link>
                {isAuth
                    ? <>
                        <Link to={'/'} className={styles.navButton}>Profile</Link>
                     </>
                    :<>
                         <Link to={'/register'} className={styles.navButton}>Register</Link>
                         <Link to={'/login'} className={styles.navButton}>Login</Link>
                    </>
                }

            </div>
        </div>
    );
};

export default Navbar;