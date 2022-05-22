using System;
using System.Collections.Generic;
using LiveChartsCore;
using LiveChartsCore.SkiaSharpView;

namespace trackR.ViewModels;

public class PlottingViewModel: ViewModelBase
{
    public PlottingViewModel()
    {
        Series = new ISeries[]
        {
            new LineSeries<int> { Values = new[] { 4, 6, 7, 1, 2, 9 }, Fill = null}
        };
        
        XAxes = new List<Axis>
        {
            new()
            {
                Labels = new[]
                {
                    DateTime.Now.AddDays(-10).ToShortDateString(),
                    DateTime.Now.AddDays(-9).ToShortDateString(),
                    DateTime.Now.AddDays(-8).ToShortDateString(),
                    DateTime.Now.AddDays(-7).ToShortDateString(),
                    DateTime.Now.AddDays(-6).ToShortDateString(),
                    DateTime.Now.AddDays(-5).ToShortDateString()
                }
            }
        };
    }
    public IEnumerable<ISeries> Series { get; set; }
    public List<Axis> XAxes { get; set; }
}