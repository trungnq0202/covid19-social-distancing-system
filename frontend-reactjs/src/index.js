import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import configureStore, { history } from './configureStore';
import App from './components/App/App';
import 'bootstrap/dist/css/bootstrap.min.css';

import './index.css';

const store = configureStore()
const render = () => {
  ReactDOM.render(
    <Provider store={store}>
      <App history={history}/>
    </Provider>,
    document.getElementById('root')
  )
}

render()

