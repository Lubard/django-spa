import styles from './../css/index.css';

var React = require('react');
var ReactDOM = require('react-dom');

var BookingItemComponent = React.createClass ({
    loadBookingItemFromServer: function(page, search_text){
        var url = '/page/BookingItemList?page='+ page + '&search_text=' + search_text;
        $.ajax({
            url: url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },
    searchBooking: function(search_text){
        this.setState({search_text: search_text, page: 1, booking_item: {}});
        this.loadBookingItemFromServer(1, search_text);
    },
    pagination: function(page){
        if (page!=this.state.page){
            this.setState({page: page, booking_item: {}});
            this.loadBookingItemFromServer(page, this.state.search_text)
        }
    },
    bookingSpecific: function(bookingID){
        var url = '/page/BookingItem/'+ bookingID + '.json';
        $.ajax({
            url: url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({booking_item: data});
            }.bind(this)
        })
    },
    getInitialState: function(){
      return {
          search_text: '',
          page: 1,
          data: [],
          booking_item: {}
      };
    },
    componentDidMount: function() {
        this.loadBookingItemFromServer(this.state.page, this.state.search_text);
    },
    render: function() {
        if (this.state.data) {
            var bookingNodes = this.state.data.map(function(bookingItem){
                // Chekc the current customer
                if (this.state.booking_item && bookingItem.id==this.state.booking_item.id){
                    // Check if user Information Existed
                    if (this.state.booking_item.booking.booker && this.state.booking_item.booking.booker.user){
                        var user = this.state.booking_item.booking.booker.user;
                        var userInfo = (
                            <p>
                                User: {user.first_name} {user.last_name}<br/>
                                Email: {user.email}
                            </p>
                        )
                    }


                    var bookingItemDetail = (
                        <tr className={styles.bookingDetails}>
                            <td colSpan="5">
                                {userInfo}
                                locked_piece_price:{this.state.booking_item.locked_piece_price}<br/>
                                locked_total_price:{this.state.booking_item.locked_total_price}<br/>
                                Spaces:{this.state.booking_item.item.spaces}<br/>
                                Product:{this.state.booking_item.item.products}
                            </td>
                        </tr>
                    )
                }
                return (
                    <tbody key={bookingItem.id}>
                        <tr onClick={() => this.bookingSpecific(bookingItem.id)}>
                            <td>{bookingItem.id}</td>
                            <td>{bookingItem.booking}</td>
                            <td>{bookingItem.quantity}</td>
                            <td>{bookingItem.item.name}</td>
                            <td>{bookingItem.item.venue.name}</td>
                        </tr>
                        {bookingItemDetail}
                    </tbody>
                );}.bind(this)
            )
        }else{
            return (<tr><td colspan="5">No items are available.</td></tr>)
        }
        return (
            <div className="booking-list">
                <SearchForm onChange={this.searchBooking}
                            search_text={this.state.search_text} />
                <table className={styles.bookingTable}>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Booking ID</th>
                            <th>QTY</th>
                            <th>Item</th>
                            <th>Venue</th>
                        </tr>
                    </thead>
                    {bookingNodes}
                </table>
                <Paginator data={this.state.data}
                           page={this.state.page}
                           onChange={this.pagination}/>
            </div>
        )
    }
});

var Paginator = React.createClass({
    pagePrevious: function(){
        var page = this.props.page;
        if(this.props.data && this.props.page>1){
            page = page - 1;
        }
        this.props.onChange(page);
    },
    pageNext: function(){
        var page = this.props.page;
        if(this.props.data && this.props.data.length==20){
            page = this.props.page + 1;
        }
        this.props.onChange(page);
    },
    render: function(){
        return (
            <div>
                <span className="step-links">
                    <a onClick={this.pagePrevious}>Previous</a>
                    <span className="current">Page {this.props.page}</span>
                    <a onClick={this.pageNext}>Next</a>
                </span>
            </div>
        );
    }
});
var SearchForm = React.createClass({
    handleInputChange: function(event) {
        this.props.onChange(event.target.value);
    },
    render: function() {
        return (
            <form className="react-form">
                <input type="text" value={this.props.search_text} onChange={this.handleInputChange} placeholder="Search for Item/Venue/Booking" />
            </form>
        );
    }
});

ReactDOM.render(<BookingItemComponent />, document.getElementById('container'));


// Transfer Code
//  ./node_modules/.bin/webpack --config webpack.config.js