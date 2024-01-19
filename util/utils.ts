import moment from "moment";

export const timeStampToDateString = (timestamp: number) => {
  return moment(timestamp).format("MMM DD YYYY");
};
