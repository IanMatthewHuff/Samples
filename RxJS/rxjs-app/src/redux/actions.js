import { ADD_CLICK } from './actionTypes';

export const addClick = (color) => ({
    type: ADD_CLICK,
    payload: { color }
});