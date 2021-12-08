import { createBrowserHistory } from "history";
import { applyMiddleware, createStore } from "redux";
import { routerMiddleware } from "connected-react-router";
import { composeWithDevTools } from "redux-devtools-extension";

import createRootReducer from "./reducers";

import thunk from "redux-thunk";

export const history = createBrowserHistory();

export default function configureStore(preloadedState) {
  const store = createStore(
    createRootReducer(history), // root reducer with router state
    composeWithDevTools(applyMiddleware(thunk, routerMiddleware(history))),
    preloadedState,
  );

  return store;
}
