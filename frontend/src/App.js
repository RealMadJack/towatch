import React, {Component} from 'react';
import Header from './components/header/Header'
import Movies from './components/movies/Movies'


class App extends Component {
  state = {};

  componentDidMount() {
  }

  render() {
    return (
      <div className="App">
        <Header />
        <Movies />
      </div>
    );
  }
}

export default App;
