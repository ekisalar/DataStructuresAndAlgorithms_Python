//console.log('Message no. 1: Sync');
//setTimeout(function() {
//   console.log('Message no. 2: setTimeout');
//}, 0);
//var promise = new Promise(function(resolve, reject) {
//   resolve();
//});
//promise.then(function(resolve) {
//   console.log('Message no. 3: 1st Promise');
//})
//.then(function(resolve) {
//   console.log('Message no. 4: 2nd Promise');
//});
//console.log('Message no. 5: Sync');




// Recursion illustration 
counter = 0 
function inception() {
   console.log (counter)
   if (counter>3) {
      return 'done'
   }
   counter ++
   return inception()
}

inception()