using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DataVisualization.Models
{
    public class Estado
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int VeryNegative { get; set; }
        public int Negative { get; set; }
        public int Neutral { get; set; }
        public int Positive { get; set; }
        public int VeryPositive { get; set; }
    }
}
