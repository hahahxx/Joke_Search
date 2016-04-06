// App component - represents the whole app
App = React.createClass({

  getInitialState: function() {
    return {data: []};
  },
  renderJokes() {
    return this.state.data.map((joke) => {
      return <Joke key={joke._id} joke={joke}/>;
    });
  },

  handleSubmit(event) {

    event.preventDefault();
    // Find the text field via the React ref
    var text = ReactDOM.findDOMNode(this.refs.textInput).value.trim();

    keyword = { data: { "query" : { "match" : { "content" : text } } } };
    HTTP.call( 'POST', 'http://localhost:9200/joke/joke_table/_search', keyword, function( error, response ) {
      if ( error ) {
        console.log( error );
      } else {
        console.log( response['data']['hits']['hits']);
        this.setState({data: response['data']['hits']['hits']});
        /*
         This will return the HTTP response object that looks something like this:
         {
           content: "String of content...",
           data: Array[100], <-- Our actual data lives here.
           headers: {  Object containing HTTP response headers }
           statusCode: 200
         }
        */
      }
    }.bind(this));


    // Clear form
    ReactDOM.findDOMNode(this.refs.textInput).value = "";
  },
  render() {
    return (
      <div className="container">
        <header>
          <h1>Joke Search</h1>
          <form className="new-joke" onSubmit={this.handleSubmit} >
            <input
              type="text"
              ref="textInput"
              placeholder="Type to get jokes" />
          </form>
        </header>
        <ul>
          {this.renderJokes()}
        </ul>
      </div>
    );
  }
});
