using DataVisualization.Database.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Text;

namespace DataVisualization.Database.BLL
{
    public class BoEstados
    {
        public List<Estados> GetAllData()
        {
            try
            {
                var context = new TweetsContext();
                var estados = new List<Estados>();

                foreach (var estado in context.Estados)
                {
                    estados.Add(estado);
                }
                return estados;
            }
            catch(Exception ex)
            {
                throw;
            }
        }

        public Estados GetDataByName(string Name)
        {
            try
            {
                var states = GetAllData();
                foreach (var state in states)
                {
                    if (state.Name == Name)
                    {
                        return state;
                    }
                }
                return null;
            }
            catch(Exception ex)
            {
                throw;
            }
        }

        public bool UpdateState(Estados estado)
        {
            try
            {
                using (var context = new TweetsContext())
                {
                    var entity = context.Estados.FirstOrDefaultAsync(item => item.Id == estado.Id).Result;
                    if(entity != null)
                    {
                        var test = context.Entry<Estados>(entity).Entity;
                        test.Negative = estado.Negative;
                        test.Neutral = estado.Neutral;
                        test.Positive = estado.Positive;
                        context.SaveChanges();
                    }
                }
                return true;
            }
            catch(Exception ex)
            {
                return false;
            }
        }
    }
}
