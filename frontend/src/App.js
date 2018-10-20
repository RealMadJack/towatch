import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Link, Switch, Redirect } from 'react-router-dom';

import Header from './components/header/Header'
import Movies from './components/movies/Movies'
import MoviePanel from './components/moviepanel/MoviePanel'
import Page404 from './components/404/Page404'


class App extends Component {
  state = {};

  componentDidMount() {
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Header />
          <Switch>
            <Route exact path="/" component={Movies} />
            <Route path="/movies/" component={MoviePanel} />
            <Route path="*" component={Page404} status={404} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
