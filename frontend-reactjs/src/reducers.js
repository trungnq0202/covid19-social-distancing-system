import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';

// import authReducer from './pages/login/login.reducer';
// import userManagementReducer from './pages/userManagement/userManagement.reducer'

const createRootReducer = (history) => combineReducers({
    // auth: authReducer,
    // userManagement: userManagementReducer,
    router: connectRouter(history)
})

export default createRootReducer