import axios from 'axios';
import React, {Component} from 'react';

import './Movies.css';

export default class Header extends Component {
	state = {
		movies: [],
	}

	componentDidMount() {
		axios.get('http://localhost:8000/api/movies/')
			.then((res) => {
				console.log(res.data)
				const movies = res.data
				this.setState({ movies })
			})
			.catch((e) => {
				console.log(e)
			})
	}

	render () {
		const movies_list = this.state.movies.map((movie) => {
			return (
				<li key={movie.id}>{movie.moviepanel.name}: {movie.name} : {movie.published_at}</li>
			);
		})

		return (
			<div className="container">
				{movies_list}
			</div>
		);
	}
}
