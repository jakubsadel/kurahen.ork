  
import React, {  } from 'react';
import './App.css';



class App extends React.Component {
	loadData() {

		const apiUrl = `http://127.0.0.1:8000/api/`;
		fetch(apiUrl)
		.then((response) => response.json())
		.then((data) => console.log(data));
	}
	render()
	{
		return <div><h1>Connection</h1></div>
	}


}
export default App;