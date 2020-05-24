using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace DataVisualization.Database.Models
{
    /// <summary>
    /// Model de banco de dados para tabela de Estados
    /// </summary>
    public partial class Estados
    {
        /// <summary>
        /// ID do estado
        /// </summary>
        [Key]
        public int Id { get; set; }
        /// <summary>
        /// Nome do estado
        /// </summary>
        [MaxLength(20)]
        public string Name { get; set; }
        /// <summary>
        /// Quantidade de registros "Negative" do estado
        /// </summary>
        public int Negative { get; set; }
        /// <summary>
        /// Quantidade de registros "Neutral" do estado
        /// </summary>
        public int Neutral { get; set; }
        /// <summary>
        /// Quantidade de registros "Positive" do estado
        /// </summary>
        public int Positive { get; set; }
    }
}
