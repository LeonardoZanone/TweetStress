using DataVisualization.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using DataVisualization.Database.BLL;

namespace DataVisualization.ViewModels
{
    public class EstadoViewModel
    {
        #region Propriedades
        public string Estado { get; set; }
        public string Sentimento { get; set; }
        #endregion

        public static Estado RetornaEstado(EstadoViewModel estadoViewModel)
        {
            var estadoDB = new Database.BLL.BoEstados().GetDataByName(estadoViewModel.Estado);
            return new Estado()
            {
                ID = estadoDB.Id,
                Name = estadoDB.Name,
                Negative = estadoDB.Negative,
                Neutral = estadoDB.Neutral,
                Positive = estadoDB.Positive
            };
        }

        public static bool AtualizarSentimento(EstadoViewModel estadoViewModel, Estado estado)
        {
            try
            {
                BoEstados boEstados = new BoEstados();
                switch (estadoViewModel.Sentimento.Trim().ToLower())
                {
                    case "very negative":
                        estado.VeryNegative++;
                        break;
                    case "negative":
                        estado.Negative++;
                        break;
                    case "neutral":
                        estado.Neutral++;
                        break;
                    case "positive":
                        estado.Positive++;
                        break;
                    case "very positive":
                        estado.VeryPositive++;
                        break;
                    default:
                        return false;
                }
                return boEstados.UpdateState(EstadoParaDB(estado));
            }
            catch(Exception ex)
            {
                return false;
            }
        }

        public static Database.Models.Estados EstadoParaDB(Estado estado)
        {
            return new Database.Models.Estados()
            {
                Id = estado.ID,
                Negative = estado.Negative,
                Neutral = estado.Neutral,
                Positive = estado.Positive
            };
        }

        //public static List<Estado> RetornaTudo()
        //{

        //}
    }
}
