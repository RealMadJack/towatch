import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Header from './components/header/Header';
import Movie from './components/movie/Movie';
import Movies from './components/movies/Movies';
import MoviePanel from './components/moviepanel/MoviePanel';
import MovieGenre from './components/moviegenre/MovieGenre';
import Page404 from './components/404/Page404';
import SignIn from './components/signin/SignIn';
import SignUp from './components/signup/SignUp';


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
            <Route exact path="/signin" component={SignIn} />
            <Route exact path="/signup" component={SignUp} />
            <Route exact path="/category/:moviegenre" component={MovieGenre} />
            <Route exact path="/:moviepanel" component={MoviePanel} />
            <Route exact path="/:moviepanel/:movie" component={Movie} />
            <Route component={Page404} status={404} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
