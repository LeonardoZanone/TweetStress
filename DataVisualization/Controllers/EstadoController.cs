using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using DataVisualization.Models;
using DataVisualization.ViewModels;
using Microsoft.AspNetCore.Mvc;

namespace DataVisualization.Controllers
{
    public class EstadoController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPut]
        public JsonResult Put(EstadoViewModel estadoViewModel)
        {
            try
            {
                if (!ModelState.IsValid)
                {
                    List<string> erros = (from item in ModelState.Values
                                        from error in item.Errors
                                        select error.ErrorMessage).ToList();
                    Response.StatusCode = 400;
                    return Json(string.Join(Environment.NewLine, erros));
                }

                Estado estado = EstadoViewModel.RetornaEstado(estadoViewModel);

                if(estado == null)
                {
                    Response.StatusCode = 404;
                    return Json("Estado não encontrado");
                }
                else
                {
                    if (EstadoViewModel.AtualizarSentimento(estadoViewModel, estado))
                        return Json("Atualizado com sucesso");
                    else
                        return Json("Erro ao atualizar");
                }
            }
            catch(Exception ex) 
            {
                Response.StatusCode = 500;
                return Json(ex.Message);
            }
        }
    }
}