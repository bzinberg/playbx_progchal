(defn sorted-wrt? [s p]
  (every? #(apply <= %)
          (->> s
               (map (zipmap p (range)))
               (remove nil?)
               (partition 2 1))))
