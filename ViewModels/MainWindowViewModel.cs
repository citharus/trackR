namespace trackR.ViewModels
{
    public class MainWindowViewModel : ViewModelBase
    {
        public MainWindowViewModel(PlottingViewModel plottingViewModel)
        {
            PlottingViewModel = plottingViewModel;
        }

        public PlottingViewModel PlottingViewModel { get; set; }
    }
}