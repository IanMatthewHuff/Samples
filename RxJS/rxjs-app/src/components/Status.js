import React from 'react';
import { connect } from 'react-redux';

const Status = ( { currentColor } ) => (
    <div>
        <h2>Status</h2>
        <h3>{currentColor}</h3>
    </div>
);

const mapStateToProps = (state) => {
    return {
        currentColor: state.countReducers.currentColor
    }
}

export default connect(mapStateToProps) (Status);