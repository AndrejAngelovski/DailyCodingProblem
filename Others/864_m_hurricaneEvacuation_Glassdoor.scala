// An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.
// For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

object Hurricane Evacuation extends App {
    def minBoats(weights: Array[Int], limit: Int): Int = {
        scala.util.Sorting.quickSort(weights)
        var i = 0
        var j = weights.length - 1
        var boats = 0
        while (i <= j) {
            if (weights(i) + weights(j) <= limit) {
                i += 1
            }
            j -= 1
            boats += 1
        }
        boats
    }

    println(minBoats(Array(100, 200, 150, 80), 200)) 
}