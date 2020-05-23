// JavaScript version

const msPerDay = 1000 * 60 * 60 * 24;
const maxCycles = 1000; 
const start = new Date(2017, 0, 11);
const today = new Date();

Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

function batteryLife(cycles) {
    const daysFromStart = Math.round((today - start) / msPerDay, 0);
   
    const maxDays = Math.round(maxCycles/(cycles/daysFromStart), 0);

    var futureDate = start.addDays(maxDays);

    return futureDate
}

futureDate = batteryLife(parseInt(process.argv[process.argv.length-1])).toDateString();
console.log('Expected day for ' + maxCycles + ' cycles: ' + futureDate + '.')


