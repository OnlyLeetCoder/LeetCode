func sumBase(n int, k int) int {
    digitSum := 0
    
    for n > 0 {
        digitSum += (n % k)
        n /= k
    }
    
    return digitSum
}